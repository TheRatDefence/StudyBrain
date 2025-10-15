"""
StudyBrain Phase 1 - Flask Application
AI-powered HSC study management system

Last edited: 9th Oct 2025
"""

#------------------| Imports |------------------#
from flask import Flask, session, render_template, request, redirect, url_for
import os





#------------------| Config |------------------#
SUBJECTS = ["Mathematics", # I do mathematics Advanced and Extension, but I just put "Mathematics" here
            "Physics",
            "Software Engineering",
            "Music",
            "English"] # I'm dropping engineering so I didn't include it



#------------------| Classes |------------------#


#------------------| Functions |------------------#
def validate_subject(subject: str) -> bool:
    """Validates a subject by checking if it's in the list of SUBJECTS
        Args:
            subject (str): The subject name to check
        Returns:
            True if subject is valid, False if subject isn't
    """
    subject = subject.title()
    return True if subject in SUBJECTS else False

def update_conversation(message_type: str, text: str) -> None | Exception:
    """Updates the conversation stored in session. Creates session if it doesn't exist yet
    Args:
        message_type (str): "user" or "ai"
        text (str): The message

    Returns:
        None or Exception
    """

    if not "conversation" in session:
        """Initialises conversation in session if it doesn't already exist"""
        print(f"Conversation in session: {session} doesn't exist, creating new one")
        session["conversation"] = []


    if message_type == "user":
        session["conversation"].append({
            "type": "user",
            "text": text
        })
        session.modified = True
        return None
    elif message_type == "ai":
        session["conversation"].append({
            "type": "ai",
            "text": text
        })
        session.modified = True
        return None
    else:
        raise Exception("Incorrect type")


#------------------| Flask Logic |------------------#
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24).hex())
app.config['SESSION_TYPE'] = 'filesystem'



@app.route('/')
def dashboard() -> str:
    """ Gets subject list from SUBJECTS list and passes the list to the dashboard template

    Returns:
        The filled in dashboard.html template
    """
    subjects_list = SUBJECTS
    return render_template('dashboard.html', subjects=subjects_list)



@app.route('/study/<subject>', methods=['GET', 'POST'])
def study_session(subject: str):
    if not validate_subject(subject):
        """Returns error html template"""
        return render_template('error.html',
                        redirect_url='/',
                        redirect_seconds=3,
                        error_title="Invalid Subject",
                        error_message=f"The subject '{subject}' could not be found. Please enter a valid subject.")


    if request.method == "POST":
        """Handles POST requests and gets the user's question from form the form"""
        # I think I'm missing some validation to check if the request contains a "question" key
        user_question = request.form.get("question")

        placeholder_ai_response = "That is a great question, here is the answer..."

        update_conversation("user", user_question)
        update_conversation("ai", placeholder_ai_response)

    elif request.method == "GET":
        if "conversation" not in session:
            session["conversation"] = []

    return render_template('study_session.html', subject=subject.title(), conversation=session["conversation"])



if __name__ == "__main__":
    app.run(debug=True, port=5001)

