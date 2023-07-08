import React from 'react'
import { useState } from 'react';
import client from './api';
import './login.css'; // Import the CSS file


export const RegisterPage = () => {
    const [currentUser, setCurrentUser] = useState();
    const [errorMessage, seterrorMessage] = useState(false);
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    function submitRegistration(e) {
        e.preventDefault();
        client.post(
          "/user/register",
          {
            email: email,
            username: username,
            password: password
          }
        ).then(function(res) {

            setCurrentUser(true);
            alert('success')
          })
      }
  return (
    <div className="main-container">

    <div className="login-container">
      <h1>Add user</h1>
      <form className="login-form" onSubmit={submitRegistration}>
        <input
          className="login-input"
          type="text"
          placeholder="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="login-input"
          type="text"
          placeholder="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className="login-input"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="login-button" type="submit">
          Add user
        </button>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
      </form>
    </div>
    </div>
  )
}
