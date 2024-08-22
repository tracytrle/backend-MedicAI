from flask import request, jsonify
from sqlalchemy import asc
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from medicai.models.conversation import Conversation
from medicai.models.user import User
from medicai.extensions import db
from medicai.conversation import bp
from datetime import datetime
import pytz

utc = pytz.UTC
@bp.route('/getLatest/<int:userId>', methods=['GET'])
@cross_origin()
def get_latest_conversation(userId):

    current_user = User.query.get(userId)
    if current_user is None:
        return jsonify(message="User not found"), 400
    # query Conversation table to get the latest conversation Id
    latest_conversation = Conversation.query.filter_by(userId=userId).order_by(Conversation.created_at.desc()).first()

    if latest_conversation is None or latest_conversation.sender: 
        # create a new conversation and return it
        new_conversation = Conversation(
            userId=userId,
            conversationId=(latest_conversation.conversationId + 1) if latest_conversation else 1,
            sender=None,
            message=None,
            created_at=datetime.now(utc),
            last_updated_at=datetime.now(utc)
        )

        db.session.add(new_conversation)
        db.session.commit()

        return jsonify(conversationId=new_conversation.conversationId), 200
    else:
        return jsonify(conversationId=latest_conversation.conversationId), 200
    
@bp.route('/addMessage/<int:userId>', methods=['POST'])
@cross_origin()
def add_message(userId):

    current_user = User.query.get(userId)
    if current_user is None:
        return jsonify(message="User not found"), 400
    
    data = request.get_json()
    if 'conversationId' not in data:
        return jsonify(message="Conversation Id is required"), 400
    if 'sender' not in data:
        return jsonify(message="Sender is required"), 400
    if 'message' not in data:
        return jsonify(message="Message is required"), 400

    # query Conversation table to get the latest conversation Id
    conversation = Conversation.query.filter_by(userId=userId, conversationId=data['conversationId']).first()

    if conversation is None:
        return jsonify(message="Conversation not found"), 400
    
    if conversation.sender is None:
        conversation.sender = data['sender']
        conversation.message = data['message']
        conversation.last_updated_at = datetime.now(utc)
    
    else :
        new_conversation = Conversation(
        userId=userId,
        conversationId=data['conversationId'],
        sender=data['sender'],
        message=data['message'],
        created_at=datetime.now(utc),
        last_updated_at=datetime.now(utc)
        )     
        db.session.add(new_conversation)
    
    db.session.commit()

    return jsonify(message="Message added successfully"), 200

@bp.route('/getAllMessages/<int:userId>', methods=['GET'])
@cross_origin()
def get_all_messages(userId):

    current_user = User.query.get(userId)
    if current_user is None:
        return jsonify(message="User not found"), 400

    # Query to group by conversationId and order by created_at
    conversations = (
        Conversation.query
        .filter_by(userId=userId)
        .order_by(asc(Conversation.conversationId), asc(Conversation.created_at))
        .all()
    )

    if not conversations:
        return jsonify(message="No conversations found"), 400

    # Grouping the results by conversationId
    grouped_conversations = {}
    for conversation in conversations:
        conv_id = conversation.conversationId
        if conv_id not in grouped_conversations:
            grouped_conversations[conv_id] = []
        grouped_conversations[conv_id].append({
            "conversationId": conversation.conversationId,
            "sender": conversation.sender,
            "message": conversation.message,
            "created_at": conversation.created_at,
            "last_updated_at": conversation.last_updated_at
        })

    # Flattening the grouped conversations into a list of dictionaries
    conversations_list = [
        {"conversationId": conv_id, "messages": msgs}
        for conv_id, msgs in grouped_conversations.items()
    ]

    return jsonify(conversations_list), 200
