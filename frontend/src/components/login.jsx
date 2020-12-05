import React, { Component } from 'react';
import GoogleLogin from 'react-google-login';

class Login extends Component {
    state = {  }
    render() { 
        return ( <div>
            <GoogleLogin
            clientId=""
            buttonText=""
            cookiePolicy="single_host_origin"
            />
        </div> );
    }
}
 
export default Login;