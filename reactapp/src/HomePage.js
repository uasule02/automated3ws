import React, { useState,useEffect } from 'react';
import client from './api';
import './home.css';
import UseCurrentUser from './UseCurrentUser';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [files, setFiles] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  function handleUpload(e) {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
  
    const authToken = localStorage.getItem('user');
    const headers = { Authorization: `Bearer ${authToken}` };
    //const config = { headers, withCredentials: true };
  
    client.post('/user/upload', {formData, withCredentials: true} )
      .then(response => {
        console.log('File uploaded successfully');
        alert('Upload successful');
        // Handle the response as needed
      })
      .catch(error => {
        console.error('File upload error:', error);
        // Handle the error as needed
      });
  }
   
  function submitLogout(e) {
    e.preventDefault();
    client.post(
      "/user/logout",
      {withCredentials: true}
    ).then(function(res) {
      setCurrentUser(false);
      localStorage.setItem('user', JSON.stringify(res.data));
      navigate('/', { replace: true });


    });
  }

  const fetchFiles = () => {
     
  };

  return (
    <div className="container">
      <div className='nav-container'>
      <UseCurrentUser />
      </div>
      <div className="upload-container">
        <h1>Upload Excel File</h1>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload} disabled={!file}>
          Upload
        </button>
        {message && <p>{message}</p>}
      </div>
      <div className="file-list-container">
        <h1>Uploaded Files</h1>
        <button onClick={fetchFiles}>Check Uploaded Files</button>
        
        {files? (
      
        <ul>
          {files.map((file, index) => (
            <li key={index}>
              <strong>File Name:</strong> {file.file_name}
              <br />
              <strong>Uploaded At:</strong> {file.uploaded_at}
              {/* Add additional file information here if needed */}
            </li>
            
          ))}
        </ul>
        ) : (
          <p>{message}</p>
          )}
      </div>
      <div>
      <form onSubmit={e => submitLogout(e)}>
           <button type="submit" variant="light">Log out</button>
      </form>
      </div>
    </div>
  );
};

export default HomePage;
