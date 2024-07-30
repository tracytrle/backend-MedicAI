from medicai.extensions import db


class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    isHeadache = db.Column(db.Boolean, nullable=True)
    isCancer = db.Column(db.Boolean, nullable=True)
    isDiabetes = db.Column(db.Boolean, nullable=True)
    isBloodClots = db.Column(db.Boolean, nullable=True)
    isArthritis = db.Column(db.Boolean, nullable=True)
    isAbnormalSkinConditions = db.Column(db.Boolean, nullable=True)
    isHighOrLowBloodPressure = db.Column(db.Boolean, nullable=True)
    isFibromyalgia = db.Column(db.Boolean, nullable=True)
    isNeckOrBackPain = db.Column(db.Boolean, nullable=True)
    isNumbness = db.Column(db.Boolean, nullable=True)
    isVaricoseVeins = db.Column(db.Boolean, nullable=True)
    isRecentInjury = db.Column(db.Boolean, nullable=True)
    isNursingOrPregnant = db.Column(db.Boolean, nullable=True)
    isDepression = db.Column(db.Boolean, nullable=True)
    isFatigue = db.Column(db.Boolean, nullable=True)
    isInsomnia = db.Column(db.Boolean, nullable=True)
    isHavingHeartDisease = db.Column(db.Boolean, nullable=True)
    isHavingSurgery = db.Column(db.Boolean, nullable=True)
    isHavingChronisIllness = db.Column(db.Boolean, nullable=True)
    isHavingHighOrLowBloodPressure = db.Column(db.Boolean, nullable=True)
    isHavingAllergies = db.Column(db.Boolean, nullable=True)
    isTakingMedication = db.Column(db.Boolean, nullable=True)
    allergies= db.Column(db.String(150), nullable=True)
    medications = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f"HealthRecord('{self.userId}')"
