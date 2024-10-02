import React, { useState } from 'react';

const Login: React.FC = () => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [loginMessage, setLoginMessage] = useState<string>('');


  const handleLogin = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (username == "admin" && password == "password") {    
        setLoginMessage("Login Success!")
    }
    else {
        setLoginMessage("Wrong Credentials!")
    }
  };

  return (
    <div>
      <h1>Login Page</h1>
      <form onSubmit={handleLogin}>
        <div>
          <label>Username: </label>
          <input 
            type="text" 
            value={username}
            onChange={(e) => setUsername(e.target.value)} 
          />
        </div>
        <div>
          <label>Password: </label>
          <input 
            type="password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)} 
          />
        </div>
        <button type="submit">Login</button>
      </form>

      {loginMessage && <div>{loginMessage}</div>}
    </div>
  );
};

export default Login;
