const date = new Date();
let day = date.getDate();
let month = date.getMonth();
let year = date.getFullYear();

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
];

const weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

const calendar = document.querySelector(".calendar");
const monthText = document.querySelector(".month h1");
const yearText = document.querySelector(".month p");
const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");
const daysContainer = document.querySelector(".days");
const objectivesContainer = document.querySelector(".objectives");

function initCalendar() {
  updateCalendar();
  prevBtn.addEventListener("click", () => {
    month--;
    if (month < 0) {
      month = 11;
      year--;
    }
    updateCalendar();
  });
  nextBtn.addEventListener("click", () => {
    month++;
    if (month > 11) {
      month = 0;
      year++;
    }
    updateCalendar();
  });
  daysContainer.addEventListener("click", e => {
    if (e.target.classList.contains("day")) {
      const selectedDate = new Date(year, month, e.target.textContent);
      const selectedDay = selectedDate.getDate();
      const selectedMonth = months[selectedDate.getMonth()];
      const selectedYear = selectedDate.getFullYear();
      const selectedWeekday = weekdays[selectedDate.getDay()];
      const selectedDateFormat = `${selectedWeekday}, ${selectedMonth} ${selectedDay}, ${selectedYear}`;
      objectivesContainer.textContent = selectedDateFormat;
    }
  });
}

function updateCalendar() {
  const firstDayOfMonth = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  monthText.textContent = months[month];
  yearText.textContent = year;
  daysContainer.innerHTML = "";
  for (let i = 0; i < firstDayOfMonth; i++) {
    const emptyDay = document.createElement("div");
    emptyDay.classList.add("empty");
    daysContainer.appendChild(emptyDay);
  }
  for (let i = 1; i <= daysInMonth; i++) {
    const day = document.createElement("div");
    day.classList.add("day");
    day.textContent = i;
    daysContainer.appendChild(day);
  }
}

initCalendar();
