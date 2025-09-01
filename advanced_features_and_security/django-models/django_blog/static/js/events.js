// ========================
// Get References
// ========================
const eventForm = document.getElementById("event-form");
const eventList = document.getElementById("event-list");

// Load existing events from localStorage or set empty array
let events = JSON.parse(localStorage.getItem("events")) || [];

// ========================
// Function to Display Events
// ========================
function displayEvents() {
    eventList.innerHTML = ""; // Clear old content

    if (events.length === 0) {
        eventList.innerHTML = "<p>No upcoming events yet. Create one above!</p>";
        return;
    }

    events.forEach((event, index) => {
        const card = document.createElement("div");
        card.classList.add("card");
        card.innerHTML = `
            <h3>${event.title}</h3>
            <small>${event.date}</small>
            <p>${event.description}</p>
            <button class="btn delete-btn" data-index="${index}">Delete</button>
        `;
        eventList.appendChild(card);
    });
}

// ========================
// Function to Add New Event
// ========================
eventForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.getElementById("event-title").value.trim();
    const date = document.getElementById("event-date").value;
    const description = document.getElementById("event-description").value.trim();

    if (title && date && description) {
        const newEvent = { title, date, description };
        events.push(newEvent);
        localStorage.setItem("events", JSON.stringify(events));
        displayEvents();
        eventForm.reset();
    }
});

// ========================
// Function to Delete Event
// ========================
eventList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
        const index = e.target.getAttribute("data-index");
        events.splice(index, 1);
        localStorage.setItem("events", JSON.stringify(events));
        displayEvents();
    }
});

// ========================
// Initial Load
// ========================
document.addEventListener("DOMContentLoaded", displayEvents);
