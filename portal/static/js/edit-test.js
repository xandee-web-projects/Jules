var questions = document.getElementById("questions");
var addQuestion = document.getElementById("add_question");
const questionTemplate = document.querySelector("[question-template]");
const optionTemplate = document.querySelector("[option-template]");

addQuestion.addEventListener("click", () => {
  let newQuestion = questionTemplate.content.cloneNode(true).children[0];
  const idx = questions.childElementCount + 1;
  newQuestion.setAttribute("questionNumber", idx);
  newQuestion.querySelector("input[type=text]").setAttribute("name", idx);
  questions.append(newQuestion);
  newQuestion
    .querySelector(".q-delete-btn")
    .addEventListener("click", (e) => newQuestion.remove());
  addOptionListener(newQuestion.querySelector(".add_option"));
});

function addOptionListener(optionBtn) {
  optionBtn.addEventListener("click", (e) => {
    let newOption = optionTemplate.content.cloneNode(true).children[0];
    const idx = `${optionBtn.parentElement.getAttribute("questionNumber")}-${
      optionBtn.previousElementSibling.childElementCount + 1
    }`;
    optionBtn.previousElementSibling.append(newOption);
    newOption.setAttribute("optionNumber", idx);
    newOption.querySelector("input[type=text]").setAttribute("name", idx);
    newOption.querySelector(".q-delete-btn").addEventListener("click", (e) => newOption.remove());
    const choose_ansBtn = newOption.querySelector(".choose-ans");
    choose_ansBtn.addEventListener("click", addChooseAnswer)
  });
}

function addChooseAnswer(e) {
    let questionOptions = this.parentElement.parentElement.parentElement.children;
    for (let i = 0; i < questionOptions.length; i++) {
      questionOptions[i].querySelector(".choose-ans").setAttribute("hidden", "true");
      questionOptions[i].querySelector(".q-delete-btn").setAttribute("disabled", "true");
    }
    this.removeAttribute("hidden");
    this.querySelector("i").innerHTML = "check_circle";
    this.removeEventListener("click", addChooseAnswer)
    this.addEventListener("click", addRemoveAnswer)
}

function addRemoveAnswer(e) {
    let questionOptions = this.parentElement.parentElement.parentElement.children;
    for (let i = 0; i < questionOptions.length; i++) {
      questionOptions[i].querySelector(".choose-ans").removeAttribute("hidden");
      questionOptions[i].querySelector(".q-delete-btn").removeAttribute("disabled");
    }
    this.querySelector("i").innerHTML = "done_outline";
    this.removeEventListener("click", addRemoveAnswer)
    this.addEventListener("click", addChooseAnswer)
}