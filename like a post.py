
@app.route('/like/<question_id>/<action>')
def like(post_id, action):
    if session.get('user'):
        post = db.session.query(Question).filter_by(id=post_id).one()
        user = db.session.query(User).filter_by(user_id=session['user_id'])

        if action == 'like':
            user.like_question(post)
            db.session.commit()
        if action == 'unlike':
            user.unlike_question(post)
            db.session.commit()

        return redirect(url_for('view_question', question_id=post_id))
    else:
        return redirect(url_for('login'))


