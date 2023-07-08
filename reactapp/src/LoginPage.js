// LoginPage.js
import React, { useState, useEffect } from 'react';
import './login.css'; // Import the CSS file
import { useNavigate } from 'react-router-dom';
import client from './api';



function LoginPage() {
  //const [currentUser, setCurrentUser] = useState('');
  const [errorMessage, seterrorMessage] = useState(false);
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const userData = localStorage.getItem('user');
    if (userData != null)   {
      setCurrentUser(JSON.parse(userData));
    }
  }, []);

  if (currentUser) {
    navigate('/home', { replace: true });
  }
  
 

  function handleSubmit(e) {
    e.preventDefault();
    client.post(
      "/user/login",
      {
        email: email,
        password: password
      }
    ).then(function(Response) {
      setCurrentUser();
      //onLogin(res.data.token); // Pass the token to the parent component
      // Save login details in cookies or local storage
      localStorage.setItem('user', JSON.stringify(Response.data));

      const udata = localStorage.getItem('user');
      setCurrentUser(JSON.parse(udata));


      alert(currentUser.username)

      navigate('/home', { replace: true });
    })
    .catch(function(res) {
      alert(res)
      //console.error(error);
      // Display an error message to the user
    });
  }
  function handleSubmit2(e){
    /* e.preventDefault();
    try {
      const response = await client.post('/api/login2/', {
        username,
        password,
      });
      console.log(response.data); // Handle successful login response
    } catch (error) {
      console.error(error); // Handle login error
    }
  };
   client.post("/user/login", { email, password })
      .then(function(res) {
        // Handle success
        alert('success')
        history.replace('/home')
      })
      .catch(function(error) {
        alert('user not found')
        console.error(error);
        // Display an error message to the user
      }); */



      
      /*const response = client.post("/user/login", { email, password })
      

      const data = response.data;

      if (data.success) {
        // Login successful, perform desired action
        alert('welcome')
      } else {
        // Login failed, display error message
        alert('invalid username')
      }
    } catch (error) {
      // Handle error
      alert('not connected')
    }*/
  };

    return (
    <div className="main-container">

    <div className="login-container">
      <h1>Login</h1>
      <form className="login-form" onSubmit={handleSubmit}>
        <input
          className="login-input"
          type="text"
          placeholder="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="login-input"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="login-button" type="submit">
          Login
        </button>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
      </form>
    </div>
    </div>
  );
};

export default LoginPage;
