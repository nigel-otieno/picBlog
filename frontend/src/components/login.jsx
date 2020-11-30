import React, { Component } from "react";
import GoogleLogin from "react-google-login";

class Login extends Component {
  state = {};
  render() {
    return (
      <div>
        <GoogleLogin
          clientId="976578575851-q4gbrnkeqnvsbqt4iqd6tu4rbb6s051e.apps.googleusercontent.com"
          buttonText="Login"
          cookiePolicy="single_host_origin"
        />
      </div>
    );
  }
}

export default Login;
