const deleteBtnGroup = document.querySelectorAll(".btn-delete");
const taskCompletedGroup = document.querySelectorAll("input[type=checkbox]");

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

deleteBtnGroup.forEach((btn) => {
  btn.addEventListener("click", () => {
    const taskId = parseInt(btn.children[0].value);
    fetch(`/delete-task/${taskId}`, {
      method: "GET",
    })
      .then(() => location.reload())
      .catch((err) => console.log(err));
  });
});

taskCompletedGroup.forEach((taskCompleted) => {
  taskCompleted.addEventListener("click", () => {
    let payload = {
      completed: taskCompleted.checked,
    };
    let data = new FormData();
    data.append("data", JSON.stringify(payload));

    fetch(`/complet-task/${taskCompleted.id}`, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: data,
    }).then((res) => console.log(res));
    // console.log(taskCompleted.checked);
  });
});
