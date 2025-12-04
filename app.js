const STATES = [
  { state: "Acre", capital: "Rio Branco" },
  { state: "Alagoas", capital: "Maceió" },
  { state: "Amapá", capital: "Macapá" },
  { state: "Amazonas", capital: "Manaus" },
  { state: "Bahia", capital: "Salvador" },
  { state: "Ceará", capital: "Fortaleza" },
  { state: "Distrito Federal", capital: "Brasília" },
  { state: "Espírito Santo", capital: "Vitória" },
  { state: "Goiás", capital: "Goiânia" },
  { state: "Maranhão", capital: "São Luís" },
  { state: "Mato Grosso", capital: "Cuiabá" },
  { state: "Mato Grosso do Sul", capital: "Campo Grande" },
  { state: "Minas Gerais", capital: "Belo Horizonte" },
  { state: "Pará", capital: "Belém" },
  { state: "Paraíba", capital: "João Pessoa" },
  { state: "Paraná", capital: "Curitiba" },
  { state: "Pernambuco", capital: "Recife" },
  { state: "Piauí", capital: "Teresina" },
  { state: "Rio de Janeiro", capital: "Rio de Janeiro" },
  { state: "Rio Grande do Norte", capital: "Natal" },
  { state: "Rio Grande do Sul", capital: "Porto Alegre" },
  { state: "Rondônia", capital: "Porto Velho" },
  { state: "Roraima", capital: "Boa Vista" },
  { state: "Santa Catarina", capital: "Florianópolis" },
  { state: "São Paulo", capital: "São Paulo" },
  { state: "Sergipe", capital: "Aracaju" },
  { state: "Tocantins", capital: "Palmas" },
];

function normalize(text) {
  return text
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .replace(/[\u0300-\u036f]/g, "")
    .trim()
    .toLowerCase();
}

function shuffle(arr) {
  return arr.slice().sort(() => Math.random() - 0.5);
}

document.addEventListener("DOMContentLoaded", () => {
  const questionEl = document.getElementById("question");
  const statusEl = document.getElementById("status");
  const answerEl = document.getElementById("answer");
  const submitBtn = document.getElementById("submit");
  const nextBtn = document.getElementById("next");
  const quitBtn = document.getElementById("quit");
  const attemptsEl = document.getElementById("attempts");
  const scoreEl = document.getElementById("score");
  const progressEl = document.getElementById("progress");
  const summarySection = document.getElementById("summary");
  const summaryText = document.getElementById("summary-text");
  const restartBtn = document.getElementById("restart");

  let deck = shuffle(STATES);
  let current = 0;
  let attempts = 3;
  let totalPoints = 0;
  let correctCount = 0;

  function updateMeta() {
    attemptsEl.textContent = `Tentativas: ${attempts}`;
    scoreEl.textContent = `Pontos: ${totalPoints}`;
    progressEl.textContent = `${current + (deck[current] ? 1 : 0)} / ${
      deck.length
    }`;
  }

  function showQuestion() {
    if (current >= deck.length) {
      finishGame();
      return;
    }
    const item = deck[current];
    statusEl.textContent = "Respondendo...";
    questionEl.textContent = `Qual a capital do Estado ${item.state}?`;
    attempts = 3;
    answerEl.value = "";
    answerEl.disabled = false;
    submitBtn.disabled = false;
    nextBtn.disabled = true;
    updateMeta();
    answerEl.focus();
  }

  function finishGame() {
    document.getElementById("game").classList.add("hidden");
    summarySection.classList.remove("hidden");
    const percent = deck.length
      ? Math.round((correctCount / deck.length) * 100)
      : 0;
    summaryText.innerHTML = `Você acertou <strong>${correctCount}</strong> de <strong>${deck.length}</strong> perguntas.<br/>Percentual: <strong>${percent}%</strong>.<br/>Pontos totais: <strong>${totalPoints}</strong>`;
  }

  function rejectAnswer() {
    attempts -= 1;
    if (attempts > 0) {
      statusEl.textContent = `Incorreto. Restam ${attempts} tentativa(s).`;
      updateMeta();
    } else {
      statusEl.innerHTML = `Esgotou as tentativas. A capital correta é <strong>${deck[current].capital}</strong>.`;
      nextBtn.disabled = false;
      answerEl.disabled = true;
      submitBtn.disabled = true;
      updateMeta();
    }
  }

  function acceptAnswer() {
    // pontos: 5 na primeira, 3 na segunda, 1 na terceira
    let pts = attempts === 3 ? 5 : attempts === 2 ? 3 : 1;
    totalPoints += pts;
    correctCount += 1;
    statusEl.innerHTML = `Correto! Você ganhou <strong>${pts}</strong> pontos.`;
    nextBtn.disabled = false;
    answerEl.disabled = true;
    submitBtn.disabled = true;
    updateMeta();
  }

  submitBtn.addEventListener("click", () => {
    const ans = normalize(answerEl.value || "");
    const correct = normalize(deck[current].capital);
    if (!ans) {
      statusEl.textContent = "Digite uma resposta antes de enviar.";
      return;
    }
    if (ans === correct) {
      acceptAnswer();
    } else {
      rejectAnswer();
    }
  });

  answerEl.addEventListener("keydown", (e) => {
    if (e.key === "Enter") submitBtn.click();
  });

  nextBtn.addEventListener("click", () => {
    current += 1;
    if (current < deck.length) {
      showQuestion();
    } else {
      finishGame();
    }
  });

  quitBtn.addEventListener("click", () => {
    finishGame();
  });

  restartBtn.addEventListener("click", () => {
    deck = shuffle(STATES);
    current = 0;
    attempts = 3;
    totalPoints = 0;
    correctCount = 0;
    document.getElementById("game").classList.remove("hidden");
    summarySection.classList.add("hidden");
    showQuestion();
  });

  // iniciar
  document.getElementById("status").textContent = "Pronto!";
  showQuestion();
});
