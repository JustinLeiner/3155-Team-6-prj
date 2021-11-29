
@app.route('/like/<question_id>/<action>')
def like(post_id, action):
    if session.get('user'):
        my_question = db.session.query(Question).filter_by(id=post_id).one()
        user = db.session.query(User).filter_by(user_id=session['user_id'])

        if action == 'like':
            user.like_question(my_question)
            db.session.commit()
        if action == 'unlike':
            user.unlike_question(my_question)
            db.session.commit()

       return render_template('selected_question.html', post=user_post, user=session['user_id'], form=form)
    else:
        return redirect(url_for('login'))


