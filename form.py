from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    SelectMultipleField,
    DateTimeField,
    BooleanField,
    TextAreaField,
)
from wtforms.validators import DataRequired, AnyOf, URL, Regexp, ValidationError


# def phoneValidation(form, phone):
#     us_phone_num = "^([0-9]{3})[-][0-9]{4}[-][0-9]{4}$"
#     match = re.search(us_phone_num, phone.data)
#     if not match:
#         raise ValidationError("Error, phone number must be in format xxx-xxx-xxxx")


# class ShowForm(FlaskForm):
#     artist_id = StringField("artist_id")
#     venue_id = StringField("venue_id")
#     start_time = DateTimeField(
#         "start_time", validators=[DataRequired()], default=datetime.today()
#     )


class MusicianForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    genres = SelectMultipleField(
        "genres",
        validators=[DataRequired()],
        choices=[
            ("Alternative", "Alternative"),
            ("Blues", "Blues"),
            ("Classical", "Classical"),
            ("Country", "Country"),
            ("Electronic", "Electronic"),
            ("Folk", "Folk"),
            ("Funk", "Funk"),
            ("Hip-Hop", "Hip-Hop"),
            ("Heavy Metal", "Heavy Metal"),
            ("Instrumental", "Instrumental"),
            ("Jazz", "Jazz"),
            ("Musical Theatre", "Musical Theatre"),
            ("Pop", "Pop"),
            ("Punk", "Punk"),
            ("R&B", "R&B"),
            ("Reggae", "Reggae"),
            ("Rock n Roll", "Rock n Roll"),
            ("Soul", "Soul"),
            ("Swing", "Swing"),
            ("Other", "Other"),
        ],
    )
    # city = StringField("city", validators=[DataRequired()])

    # state = SelectField(
    #     "state",
    #     validators=[DataRequired()],
    #     choices=[
    #         ("AL", "AL"),
    #         ("AK", "AK"),
    #         ("AZ", "AZ"),
    #         ("AR", "AR"),
    #         ("CA", "CA"),
    #         ("CO", "CO"),
    #         ("CT", "CT"),
    #         ("DE", "DE"),
    #         ("DC", "DC"),
    #         ("FL", "FL"),
    #         ("GA", "GA"),
    #         ("HI", "HI"),
    #         ("ID", "ID"),
    #         ("IL", "IL"),
    #         ("IN", "IN"),
    #         ("IA", "IA"),
    #         ("KS", "KS"),
    #         ("KY", "KY"),
    #         ("LA", "LA"),
    #         ("ME", "ME"),
    #         ("MT", "MT"),
    #         ("NE", "NE"),
    #         ("NV", "NV"),
    #         ("NH", "NH"),
    #         ("NJ", "NJ"),
    #         ("NM", "NM"),
    #         ("NY", "NY"),
    #         ("NC", "NC"),
    #         ("ND", "ND"),
    #         ("OH", "OH"),
    #         ("OK", "OK"),
    #         ("OR", "OR"),
    #         ("MD", "MD"),
    #         ("MA", "MA"),
    #         ("MI", "MI"),
    #         ("MN", "MN"),
    #         ("MS", "MS"),
    #         ("MO", "MO"),
    #         ("PA", "PA"),
    #         ("RI", "RI"),
    #         ("SC", "SC"),
    #         ("SD", "SD"),
    #         ("TN", "TN"),
    #         ("TX", "TX"),
    #         ("UT", "UT"),
    #         ("VT", "VT"),
    #         ("VA", "VA"),
    #         ("WA", "WA"),
    #         ("WV", "WV"),
    #         ("WI", "WI"),
    #         ("WY", "WY"),
    #     ],
    # )
    e_mail = StringField("e_mail", validators=[DataRequired()])

    avatar_link = StringField("avatar_link", validators=[URL()])

    phone = StringField("phone", validators=[DataRequired()])

    website = StringField("website", validators=[URL()])

    introduction = StringField("introduction")




class SongForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    
    musician_id = StringField("musician_id", validators=[DataRequired()])

    # city = StringField("city", validators=[DataRequired()])

    # state = SelectField(
    #     "state",
    #     validators=[DataRequired()],
    #     choices=[
    #         ("AL", "AL"),
    #         ("AK", "AK"),
    #         ("AZ", "AZ"),
    #         ("AR", "AR"),
    #         ("CA", "CA"),
    #         ("CO", "CO"),
    #         ("CT", "CT"),
    #         ("DE", "DE"),
    #         ("DC", "DC"),
    #         ("FL", "FL"),
    #         ("GA", "GA"),
    #         ("HI", "HI"),
    #         ("ID", "ID"),
    #         ("IL", "IL"),
    #         ("IN", "IN"),
    #         ("IA", "IA"),
    #         ("KS", "KS"),
    #         ("KY", "KY"),
    #         ("LA", "LA"),
    #         ("ME", "ME"),
    #         ("MT", "MT"),
    #         ("NE", "NE"),
    #         ("NV", "NV"),
    #         ("NH", "NH"),
    #         ("NJ", "NJ"),
    #         ("NM", "NM"),
    #         ("NY", "NY"),
    #         ("NC", "NC"),
    #         ("ND", "ND"),
    #         ("OH", "OH"),
    #         ("OK", "OK"),
    #         ("OR", "OR"),
    #         ("MD", "MD"),
    #         ("MA", "MA"),
    #         ("MI", "MI"),
    #         ("MN", "MN"),
    #         ("MS", "MS"),
    #         ("MO", "MO"),
    #         ("PA", "PA"),
    #         ("RI", "RI"),
    #         ("SC", "SC"),
    #         ("SD", "SD"),
    #         ("TN", "TN"),
    #         ("TX", "TX"),
    #         ("UT", "UT"),
    #         ("VT", "VT"),
    #         ("VA", "VA"),
    #         ("WA", "WA"),
    #         ("WV", "WV"),
    #         ("WI", "WI"),
    #         ("WY", "WY"),
    #     ],
    # )

    # phone = StringField(
    #     "phone",
    #     validators=[DataRequired()],
    # )

    # image_link = StringField("image_link")

    genres = SelectMultipleField(
        "genres",
        validators=[DataRequired()],
        choices=[
            ("Alternative", "Alternative"),
            ("Blues", "Blues"),
            ("Classical", "Classical"),
            ("Country", "Country"),
            ("Electronic", "Electronic"),
            ("Folk", "Folk"),
            ("Funk", "Funk"),
            ("Hip-Hop", "Hip-Hop"),
            ("Heavy Metal", "Heavy Metal"),
            ("Instrumental", "Instrumental"),
            ("Jazz", "Jazz"),
            ("Musical Theatre", "Musical Theatre"),
            ("Pop", "Pop"),
            ("Punk", "Punk"),
            ("R&B", "R&B"),
            ("Reggae", "Reggae"),
            ("Rock n Roll", "Rock n Roll"),
            ("Soul", "Soul"),
            ("Swing", "Swing"),
            ("Other", "Other"),
        ],
    )

    # facebook_link = StringField(
    #     "facebook_link",
    #     validators=[URL()],
    # )

    song_link = StringField("song_link", validators=[URL()])

    cover_link = StringField("cover_link", validators=[URL()])

    introduction = StringField("introduction")
