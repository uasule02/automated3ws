
import React, { useState, useEffect } from 'react';
import client from './api';

const UseCurrentUser = () => {
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const userData = localStorage.getItem('user');
    if (userData) {
      setCurrentUser(JSON.parse(userData));
    }
  }, []);

  if (!currentUser) {
    return <div>No user logged in</div>;
  
  }

  return (
    <div>
      <h1>Welcome, {currentUser.usename}</h1>
      <p>Email: {currentUser.email}</p>
    </div>
  );
};

export default UseCurrentUser;

/*import { useState, useEffect } from 'react';
import client from './api';
function useCurrentUser(){
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    client
      .get('/user/current_user')
      .then((response) => {
        setCurrentUser(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return currentUser;
}; */

