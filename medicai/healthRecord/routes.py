from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from medicai.models.healthRecord import HealthRecord
from medicai.extensions import db
from medicai.extensions import bcrypt
from medicai.healthRecord import bp


@bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.get_json()
    if 'userId' not in data:
        return jsonify(message="User ID is required"), 400
    
    user_exists = HealthRecord.query.filter_by(userId=data['userId']).first() is not None
    if user_exists:
        return jsonify(message="Health record already exists"), 409

    new_health_record = HealthRecord(
        userId=data['userId'],
        isHeadache=data.get('isHeadache', False),
        isCancer=data.get('isCancer', False),
        isDiabetes=data.get('isDiabetes', False),
        isBloodClots=data.get('isBloodClots', False),
        isArthritis=data.get('isArthritis', False),
        isAbnormalSkinConditions=data.get('isAbnormalSkinConditions', False),
        isHighOrLowBloodPressure=data.get('isHighOrLowBloodPressure', False),
        isFibromyalgia=data.get('isFibromyalgia', False),
        isNeckOrBackPain=data.get('isNeckOrBackPain', False),
        isNumbness=data.get('isNumbness', False),
        isVaricoseVeins=data.get('isVaricoseVeins', False),
        isRecentInjury=data.get('isRecentInjury', False),
        isNursingOrPregnant=data.get('isNursingOrPregnant', False),
        isDepression=data.get('isDepression', False),
        isFatigue=data.get('isFatigue', False),
        isInsomnia=data.get('isInsomnia', False),
        isHavingHeartDisease=data.get('isHavingHeartDisease', False),
        isHavingSurgery=data.get('isHavingSurgery', False),
        isHavingChronisIllness=data.get('isHavingChronisIllness', False),
        isHavingHighOrLowBloodPressure=data.get('isHavingHighOrLowBloodPressure', False),
        isHavingAllergies=data.get('isHavingAllergies', False),
        isTakingMedication=data.get('isTakingMedication', False),
        allergies=data.get('allergies', ''),
        medications=data.get('medications', '')
    )
    
    db.session.add(new_health_record)
    db.session.commit()
    return jsonify({
        "id": new_health_record.id,
        "userId": new_health_record.userId   
    })

   