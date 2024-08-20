document.addEventListener("DOMContentLoaded", function () {
  const deadlineElements = document.querySelectorAll(".deadline");
  deadlineElements.forEach((element) => {
    const deadlineDate = new Date(element.textContent.replace("Due: ", ""));
    const now = new Date();
    const timeDifference = deadlineDate - now;
    const daysUntilDeadline = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));

    if (daysUntilDeadline <= 3) {
      element.style.color = "#ff4d4d";
      element.style.fontWeight = "bold";
      alert(`Reminder: ${element.textContent}`);
    }
  });

  const sortable = new Sortable(document.querySelector("#task-list"), {
    animation: 150,
    onEnd: function (evt) {
      // Handle sorting and save order if needed
      console.log("Item moved", evt);
    },
  });
});
