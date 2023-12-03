let currentQuestionIndex = 0;
let score = 0;
const questions = [
    {
        question: "What does the term 'AI' stand for in the context of robotics?",
        answers: ["A) Advanced Intelligence", "B) Artificial Insight", "C) Automated Interaction", "D) Artificial Intelligence"],
        correct: 3
    },
    {
        question: "Which programming language is commonly used in robotics development?",
        answers: ["A) Java", "B) Python", "C) C++", "D) Ruby"],
        correct: 2
    },
    {
        question: "What does the acronym 'ROS' stand for in robotics?",
        answers: ["A) Robotic Operating System", "B) Realistic Object Simulation", "C) Robust Object Sensing", "D) Responsive Orientation System"],
        correct: 0
    },
    {
        question: "Which sensor is commonly used in robotics for distance measurement?",
        answers: ["A) Gyroscope", "B) Accelerometer", "C) LIDAR", "D) Thermocouple"],
        correct: 2
    },
    {
        question: "What is the purpose of a robotic manipulator in industrial robotics?",
        answers: ["A) Visual Perception", "B) Object Grasping and Manipulation", "C) Speech Recognition", "D) Motion Planning and Control"],
        correct: 1
    }
];

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
}

function nextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        displayQuestion();
    } else {
        document.getElementById("quiz-container").innerHTML = `<h1>Your score: ${score}/${questions.length}</h1>`;
    }
}

// Start the quiz
displayQuestion();
