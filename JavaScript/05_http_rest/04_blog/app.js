function attachEvents() {
  const POSTS_URL = "http://localhost:3030/jsonstore/blog/posts";
  const COMMENT_URL = "http://localhost:3030/jsonstore/blog/comments";
  const loadPostsBtn = document.getElementById("btnLoadPosts");
  const viewPostBtn = document.getElementById("btnViewPost");
  const selectMenu = document.getElementById("posts");
  const postTitle = document.getElementById("post-title");
  const postBody = document.getElementById("post-body");
  const postComments = document.getElementById("post-comments");

  var postsCollection = {};

  loadPostsBtn.addEventListener("click", loadPosts);
  viewPostBtn.addEventListener("click", viewPost);

  async function loadPosts() {
    let request = await fetch(POSTS_URL);
    let posts = await request.json();

    for (const post in posts) {
      let { body, id, title } = posts[post];
      let newOption = document.createElement("option");
      postsCollection[id] = body;
      newOption.setAttribute("value", `${id}`);
      newOption.textContent = title;
      selectMenu.appendChild(newOption);
    }
  }

  async function viewPost() {
    postComments.textContent = "";
    let request = await fetch(COMMENT_URL);
    let allComments = await request.json();
    let comments = {};

    let searchedPost = selectMenu.value;

    for (const comment in allComments) {
      let { id, postId, text } = allComments[comment];
      if (searchedPost === postId) {
        comments[id] = text;
      }
    }

    postTitle.textContent = selectMenu.options[selectMenu.selectedIndex].text;
    postBody.textContent = postsCollection[searchedPost];

    for (const com in comments) {
      let newLi = document.createElement("li");
      newLi.id = com;
      newLi.textContent = comments[com];
      postComments.appendChild(newLi);
    }
  }
}

attachEvents();
