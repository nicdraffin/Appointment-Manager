class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self._client_name = ""
        self._client_phone = ""
        self._appt_type = 0
        self._day_of_week = day_of_week
        self._start_time_hour = start_time_hour

    def get_client_name(self):
        return self._client_name

    def get_client_phone(self):
        return self._client_phone

    def get_appt_type(self):
        return self._appt_type

    def get_day_of_week(self):
        return self._day_of_week

    def get_start_time_hour(self):
        return self._start_time_hour

    def get_appt_type_desc(self):
        types = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return types.get(self._appt_type, "Unknown")

    def get_end_time_hour(self):
        return self._start_time_hour + 1

    def set_client_name(self, client_name):
        self._client_name = client_name

    def set_client_phone(self, client_phone):
        self._client_phone = client_phone

    def set_appt_type(self, appt_type):
        self._appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self._client_name = ""
        self._client_phone = ""
        self._appt_type = 0

    def format_record(self):
        return f"{self._client_name},{self._client_phone},{self._appt_type},{self._day_of_week},{self._start_time_hour:02d}"

    def __str__(self):
        return "{:<20s}{:<15s}{:<10s}{:02d}:00  -  {:02d}:00     {:<20s}".format(self._client_name, self._client_phone, self._day_of_week, self._start_time_hour, self.get_end_time_hour(), self.get_appt_type_desc())