// ========================
// Get References
// ========================
const blogForm = document.getElementById("blog-form");
const blogList = document.getElementById("blog-list");

// Load existing posts from localStorage or set empty array
let blogs = JSON.parse(localStorage.getItem("blogs")) || [];

// ========================
// Function to Display Blogs
// ========================
function displayBlogs() {
    blogList.innerHTML = ""; // Clear old content

    if (blogs.length === 0) {
        blogList.innerHTML = "<p>No blog posts yet. Create one above!</p>";
        return;
    }

    blogs.forEach((blog, index) => {
        const card = document.createElement("div");
        card.classList.add("card");
        card.innerHTML = `
            <h3>${blog.title}</h3>
            <small>${blog.date}</small>
            <p>${blog.content}</p>
            <button class="btn delete-btn" data-index="${index}">Delete</button>
        `;
        blogList.appendChild(card);
    });
}

// ========================
// Function to Add New Blog
// ========================
blogForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.getElementById("blog-title").value.trim();
    const content = document.getElementById("blog-content").value.trim();
    const date = new Date().toISOString().split("T")[0]; // current date

    if (title && content) {
        const newBlog = { title, content, date };
        blogs.push(newBlog);
        localStorage.setItem("blogs", JSON.stringify(blogs));
        displayBlogs();
        blogForm.reset();
    }
});

// ========================
// Function to Delete Blog
// ========================
blogList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
        const index = e.target.getAttribute("data-index");
        blogs.splice(index, 1);
        localStorage.setItem("blogs", JSON.stringify(blogs));
        displayBlogs();
    }
});

// ========================
// Initial Load
// ========================
document.addEventListener("DOMContentLoaded", displayBlogs);
