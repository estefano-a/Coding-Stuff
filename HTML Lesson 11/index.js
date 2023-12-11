let currentQuestionIndex = 0;
let score = 0;
let questions = [];
let timer;
let timeLeft = 30;

async function loadQuestions() {
    try {
        const response = await fetch('questions.json');
        const data = await response.json();
        questions = data.questions;
    } catch (error) {
        console.error("Error loading questions:", error);
    }
}

async function initQuiz() {
    await loadQuestions();
    loadProgress();
    if (questions.length === 0) {
        return;
    }
    displayQuestion(); // Optionally start the quiz here or wait for a button click
}

function startTimer() {
    timer = setInterval(() => {
        timeLeft--;
        updateTimerDisplay();

        if (timeLeft <= 0) {
            clearInterval(timer);
            resetTimer();
            nextQuestion();
        }
    }, 1000);
}

function updateTimerDisplay() {
    document.getElementById("timer").textContent = timeLeft;
}

function stopTimer() {
    clearInterval(timer);
}

function resetTimer() {
    timeLeft = 30;
}

function saveProgress() {
    localStorage.setItem('quizProgress', JSON.stringify({ currentQuestionIndex, score }));
}

function loadProgress() {
    const progress = JSON.parse(localStorage.getItem('quizProgress'));
    if (progress) {
        currentQuestionIndex = progress.currentQuestionIndex;
        score = progress.score;
    }
}

document.getElementById("startButton").addEventListener("click", function() {
    startQuiz();
});

function startQuiz() {
    document.getElementById("startButton").style.display = 'none';
    startTimer();
    displayQuestion();
}

function displayQuestion() {
    const question = questions[currentQuestionIndex];
    document.getElementById("question").textContent = question.question;
    const answerList = document.getElementById("answer-list");
    answerList.innerHTML = '';

    question.answers.forEach((answer, index) => {
        const li = document.createElement("li");
        li.textContent = answer;
        li.onclick = () => selectAnswer(index);
        answerList.appendChild(li);
    });
}

function selectAnswer(index) {
    const isCorrect = questions[currentQuestionIndex].correct === index;
    const selectedAnswer = document.querySelectorAll("#answer-list li")[index];
    if (isCorrect) {
        score++;
        selectedAnswer.classList.add("correct");
    } else {
        selectedAnswer.classList.add("incorrect");
    }
    document.querySelectorAll("#answer-list li").forEach(li => li.onclick = null);
    setTimeout(nextQuestion, 1000); // Add a delay before next question
}

function nextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        displayQuestion();
    } else {
        stopTimer(); // Stop the timer
        hideTimer(); // Hide the timer display
        document.getElementById("quiz-container").innerHTML = `<h1 class="result">Your score: ${score}/${questions.length}</h1>`;
    }
}

function hideTimer() {
    document.getElementById("timer").style.display = 'none';
}


// Initialize the quiz
initQuiz();
