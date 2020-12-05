import React, { Component } from "react";
import Like from './Like'


class Post extends Component {
  state = {};
  render() {
    return (
      <article className="Post" ref="Post">
        <header>
          <div className="Post-user">
            <div className="Post-user-avatar">
              <img
                src="https://news.artnet.com/app/news-upload/2019/12/5db820a075ba3.jpg"
                alt="Chris"
              />
            </div>
            <div className="Post-user-nickname">
              <span>Chris</span>
            </div>
          </div>
        </header>
        <div className="Post-image">
          <div className="Post-image-bg">
            <img
              alt="Icon Living"
              src="https://news.artnet.com/app/news-upload/2019/12/5db820a075ba3.jpg"
            />
          </div>
        </div>
        <div className="Post-caption">
          <Like />
        </div>
      </article>
    );
  }
}

export default Post;
