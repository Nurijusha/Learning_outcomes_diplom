import React from "react";
import Button from '@mui/material/Button';
import {
  useNavigate,
  useLocation,
} from "react-router-dom";
import '../App.css';

function SendEmail() {
  const navigate = useNavigate();
  const search = useLocation().search;
  const email = new URLSearchParams(search).get("email");

  return (
    <div className="contentCenter">
      <div className="authBlock">
        <h2>Подтверждение email</h2>
        На ваш email: {email} был отправлена ссылка для подтверждения, пройдите по ней для регистрации!
        <Button variant="outlined" onClick={() => navigate("/")} >Назад</Button>
      </div>
    </div>
  );
}

export default SendEmail;
