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

@bp.route('/getRecord/<int:userId>', methods=['GET'])
@cross_origin()
def get_record(userId):
    health_record = HealthRecord.query.filter_by(userId=userId).first()
    if health_record is None:
        return jsonify(message="Health record not found"), 404
    
    return jsonify({
        "id": health_record.id,
        "userId": health_record.userId,
        "isHeadache": health_record.isHeadache,
        "isCancer": health_record.isCancer,
        "isDiabetes": health_record.isDiabetes,
        "isBloodClots": health_record.isBloodClots,
        "isArthritis": health_record.isArthritis,
        "isAbnormalSkinConditions": health_record.isAbnormalSkinConditions,
        "isHighOrLowBloodPressure": health_record.isHighOrLowBloodPressure,
        "isFibromyalgia": health_record.isFibromyalgia,
        "isNeckOrBackPain": health_record.isNeckOrBackPain,
        "isNumbness": health_record.isNumbness,
        "isVaricoseVeins": health_record.isVaricoseVeins,
        "isRecentInjury": health_record.isRecentInjury,
        "isNursingOrPregnant": health_record.isNursingOrPregnant,
        "isDepression": health_record.isDepression,
        "isFatigue": health_record.isFatigue,
        "isInsomnia": health_record.isInsomnia,
        "isHavingHeartDisease": health_record.isHavingHeartDisease,
        "isHavingSurgery": health_record.isHavingSurgery,
        "isHavingChronisIllness": health_record.isHavingChronisIllness,
        "isHavingHighOrLowBloodPressure": health_record.isHavingHighOrLowBloodPressure,
        "isHavingAllergies": health_record.isHavingAllergies,
        "isTakingMedication": health_record.isTakingMedication,
        "allergies": health_record.allergies,
        "medications": health_record.medications
    })
@bp.route('/updateRecord/<int:userId>', methods=['PUT'])
@cross_origin()
def update_record(userId):
    health_record = HealthRecord.query.filter_by(userId=userId).first()
    if health_record is None:
        return jsonify(message="Health record not found"), 404
    
    data = request.get_json()
    health_record.isHeadache = data.get('isHeadache', health_record.isHeadache)
    health_record.isCancer = data.get('isCancer', health_record.isCancer)
    health_record.isDiabetes = data.get('isDiabetes', health_record.isDiabetes)
    health_record.isBloodClots = data.get('isBloodClots', health_record.isBloodClots)
    health_record.isArthritis = data.get('isArthritis', health_record.isArthritis)
    health_record.isAbnormalSkinConditions = data.get('isAbnormalSkinConditions', health_record.isAbnormalSkinConditions)
    health_record.isHighOrLowBloodPressure = data.get('isHighOrLowBloodPressure', health_record.isHighOrLowBloodPressure)
    health_record.isFibromyalgia = data.get('isFibromyalgia', health_record.isFibromyalgia)
    health_record.isNeckOrBackPain = data.get('isNeckOrBackPain', health_record.isNeckOrBackPain)
    health_record.isNumbness = data.get('isNumbness', health_record.isNumbness)
    health_record.isVaricoseVeins = data.get('isVaricoseVeins', health_record.isVaricoseVeins)
    health_record.isRecentInjury = data.get('isRecentInjury', health_record.isRecentInjury)
    health_record.isNursingOrPregnant = data.get('isNursingOrPregnant', health_record.isNursingOrPregnant)
    health_record.isDepression = data.get('isDepression', health_record.isDepression)
    health_record.isFatigue = data.get('isFatigue', health_record.isFatigue)
    health_record.isInsomnia = data.get('isInsomnia', health_record.isInsomnia)
    health_record.isHavingHeartDisease = data.get('isHavingHeartDisease', health_record.isHavingHeartDisease)
    health_record.isHavingSurgery = data.get('isHavingSurgery', health_record.isHavingSurgery)
    health_record.isHavingChronisIllness = data.get('isHavingChronisIllness', health_record.isHavingChronisIllness)
    health_record.isHavingHighOrLowBloodPressure = data.get('isHavingHighOrLowBloodPressure', health_record.isHavingHighOrLowBloodPressure)
    health_record.isHavingAllergies = data.get('isHavingAllergies', health_record.isHavingAllergies)
    health_record.isTakingMedication = data.get('isTakingMedication', health_record.isTakingMedication)
    health_record.allergies = data.get('allergies', health_record.allergies)
    health_record.medications = data.get('medications', health_record.medications)

    db.session.commit()


    return jsonify({
        "id": health_record.id,
        "userId": health_record.userId
    }), 200

                                                    


   