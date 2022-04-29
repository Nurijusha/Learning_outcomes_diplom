import React from "react";
import Button from '@mui/material/Button';
import {
  useNavigate
} from "react-router-dom";
import '../App.css';

function SendEmail() {
  const navigate = useNavigate();

  return (
    <div className="contentCenter">
      <div className="authBlock">
        <h2>Подтверждение email</h2>
        На ваш email: nurijusha@gmail.com был отправлена ссылка для подтверждения, пройдите по ней для регистрации!
        <Button variant="outlined" onClick={() => navigate("/")} >Назад</Button>
      </div>
    </div>
  );
}

export default SendEmail;
