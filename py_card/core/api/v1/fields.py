import calendar

from datetime import datetime

from rest_framework import serializers


class MonthYearSerializerField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            date_obj = datetime.strptime(data, "%m/%Y").date().replace(day=1)
            _, last_day = calendar.monthrange(date_obj.year, date_obj.month)
        except ValueError:
            raise serializers.ValidationError("Invalid date. Use MM/YYYY format.")

        if date_obj < datetime.now().date():
            raise serializers.ValidationError("Expired date.")

        return date_obj.replace(day=last_day)

    def to_representation(self, value):
        return value.strftime("%m/%Y")
