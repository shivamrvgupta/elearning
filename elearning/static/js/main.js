console.log("Hello World");

const modalBtns = [...document.getElementsByClassName("modal-button")];
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href


modalBtns.forEach((modalBtn) =>
  modalBtn.addEventListener("click", () => {
    const pk = modalBtn.getAttribute('data-pk')
    const quiz = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-question')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const time = modalBtn.getAttribute('data-time')
    const pass = modalBtn.getAttribute('data-pass')

    modalBody.innerHTML = `
      <div class="h5 mb-3 mr-3"> Are you sure you want to begin ${quiz}?</div>
      <div class="text-muted ml-4">
        <ul>
            <li>difficulty: <b>${difficulty}</b></li>
            <li>Number of Questions: <b>${numQuestions}</b></li>
            <li>Score to Pass: <b>${pass}</b></li>
            <li>time: <b>${time} min</b></li>
        </ul>
      </div>
      `

    startBtn.addEventListener('click', ()=>{
      window.location.href = url + pk
      console.log(window.location.href)
    })
}))
