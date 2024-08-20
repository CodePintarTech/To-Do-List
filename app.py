from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Menyimpan tugas dalam format: {"task": "Task description", "category": "Category", "priority": "Priority", "recurring": True/False, "deadline": "YYYY-MM-DD"}
tasks = []

categories = ["Work", "Personal", "Shopping"]
priorities = ["Low", "Medium", "High"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add' in request.form:
            task = request.form['task']
            category = request.form['category']
            priority = request.form['priority']
            recurring = 'recurring' in request.form
            deadline = request.form.get('deadline')
            if task and category and priority:
                tasks.append({"task": task, "category": category, "priority": priority, "recurring": recurring, "deadline": deadline})
        elif 'remove' in request.form:
            task_index = int(request.form['task_index'])
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
        return redirect(url_for('index'))
    
    filter_category = request.args.get('category')
    filter_priority = request.args.get('priority')
    
    filtered_tasks = [task for task in tasks if (not filter_category or task['category'] == filter_category) and (not filter_priority or task['priority'] == filter_priority)]
    return render_template('index.html', tasks=filtered_tasks, categories=categories, priorities=priorities)

if __name__ == '__main__':
    app.run(debug=True)
