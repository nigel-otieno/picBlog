import React, { Component } from "react";
import { Button } from "react-bootstrap";

// input: liked: boolean
// output: onClick event

class Like extends Component {
  state = {
    likes: 0
  };
  addLike = () => {
    let newLike = this.state.likes + 1;
    this.setState({
      likes: newLike
    });
  };
  render() {
    return (
      <Button className="" aria-hidden="true" onClick={this.addLike}>
        Likes: {this.state.likes}{" "}
      </Button>
    );
  }
}

export default Like;
