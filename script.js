async function loadTasks() {

    const response =
        await fetch("/tasks");

    const tasks =
        await response.json();

    const container =
        document.getElementById("tasks");

    container.innerHTML = "";

    tasks.forEach(task => {

        const taskElement =
            document.createElement("div");

        taskElement.className =
            task.completed
                ? "task completed"
                : "task";

        const titleElement =
            document.createElement("span");

        titleElement.className = "task-title";
        titleElement.textContent = task.title;

        const actionsElement =
            document.createElement("div");

        actionsElement.className = "actions";

        actionsElement.append(
            createActionButton(
                "complete-btn",
                "complete",
                "Complete task",
                () => toggleTask(task.id)
            ),
            createActionButton(
                "edit-btn",
                "edit",
                "Edit task",
                () => editTask(task)
            ),
            createActionButton(
                "delete-btn",
                "delete",
                "Delete task",
                () => deleteTask(task.id)
            )
        );

        taskElement.append(
            titleElement,
            actionsElement
        );

        container.appendChild(taskElement);

    });
}


const icons = {
    complete: `
        <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M20.3 6.3 9 17.6l-5.3-5.3 2.1-2.1L9 13.4l9.2-9.2z"></path>
        </svg>
    `,
    edit: `
        <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M4 17.8V21h3.2L18.6 9.6l-3.2-3.2L4 17.8z"></path>
            <path d="M20.7 7.5c.4-.4.4-1 0-1.4l-2.8-2.8c-.4-.4-1-.4-1.4 0l-1.4 1.4 4.2 4.2 1.4-1.4z"></path>
        </svg>
    `,
    delete: `
        <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M7 21c-1.1 0-2-.9-2-2V8h14v11c0 1.1-.9 2-2 2H7z"></path>
            <path d="M9 4h6l1 2h4v2H4V6h4l1-2z"></path>
            <path d="M9 10h2v8H9v-8zm4 0h2v8h-2v-8z"></path>
        </svg>
    `
};


function createActionButton(className, iconName, label, onClick) {

    const button =
        document.createElement("button");

    button.className = className;
    button.type = "button";
    button.title = label;
    button.setAttribute("aria-label", label);
    button.innerHTML = icons[iconName];
    button.addEventListener("click", onClick);

    return button;
}


async function addTask() {

    const title =
        document.getElementById(
            "taskInput"
        ).value;

    if (!title.trim()) {

        alert("Enter Task");

        return;
    }

    await fetch("/add-task", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({
            title: title.trim()
        })
    });

    document.getElementById(
        "taskInput"
    ).value = "";

    loadTasks();
}


async function toggleTask(id) {

    await fetch("/toggle-task", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({
            id: id
        })
    });

    loadTasks();
}


async function editTask(task) {

    const title =
        prompt("Edit task", task.title);

    if (title === null) {

        return;
    }

    if (!title.trim()) {

        alert("Task cannot be empty");

        return;
    }

    await fetch("/update-task", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({
            id: task.id,
            title: title.trim()
        })
    });

    loadTasks();
}


async function deleteTask(id) {

    await fetch("/delete-task", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({
            id: id
        })
    });

    loadTasks();
}


document
    .getElementById("taskInput")
    .addEventListener("keydown", event => {

        if (event.key === "Enter") {

            addTask();

        }
    });

loadTasks();
