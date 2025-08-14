// ========================
// Sample Data (Temporary)
// ========================
const sampleBlogs = [
    {
        title: "How to Grow Your Audience",
        content: "Learn strategies to grow your audience with organic engagement and smart collaborations.",
        date: "2025-08-01"
    },
    {
        title: "Top 5 Content Creation Tools",
        content: "Discover the best tools that can make your content creation process easier and faster.",
        date: "2025-08-10"
    }
];

const sampleEvents = [
    {
        title: "Content Creators Meetup",
        date: "2025-09-05",
        description: "Join fellow creators for a day of networking, workshops, and fun."
    },
    {
        title: "Live Streaming Masterclass",
        date: "2025-09-20",
        description: "A free online session teaching tips & tricks to improve your live streams."
    }
];

// ========================
// Function to Render Cards
// ========================
function renderCards(containerId, data, type) {
    const container = document.getElementById(containerId);
    container.innerHTML = ""; // Clear old content

    data.forEach(item => {
        const card = document.createElement("div");
        card.classList.add("card");

        if (type === "blog") {
            card.innerHTML = `
                <h3>${item.title}</h3>
                <small>${item.date}</small>
                <p>${item.content}</p>
                <a href="blog.html" class="btn">Read More</a>
            `;
        } else if (type === "event") {
            card.innerHTML = `
                <h3>${item.title}</h3>
                <small>${item.date}</small>
                <p>${item.description}</p>
                <a href="events.html" class="btn">View Details</a>
            `;
        }

        container.appendChild(card);
    });
}

// ========================
// Load Content on Page Load
// ========================
document.addEventListener("DOMContentLoaded", () => {
    renderCards("blog-preview", sampleBlogs, "blog");
    renderCards("event-preview", sampleEvents, "event");
});
