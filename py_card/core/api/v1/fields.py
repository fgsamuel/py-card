import calendar

from datetime import datetime

from rest_framework import serializers


class MonthYearSerializerField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            date_obj = datetime.strptime(data, "%m/%Y").date().replace(day=1)
            _, last_day = calendar.monthrange(date_obj.year, date_obj.month)
            return date_obj.replace(day=last_day)
        except ValueError:
            raise serializers.ValidationError("Invalid date. Use MM/YYYY format.")

    def to_representation(self, value):
        return value.strftime("%m/%Y")
