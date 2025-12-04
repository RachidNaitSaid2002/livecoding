'use client'
import Image from "next/image";
import { useState } from "react";


export default function Home() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  const login = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:8000/login',{
      method:'POST',
      headers: {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify({
        "email": email,
        "password": password
      })
    })

    const data = await response.json()
    
    setMessage(data.message)
    const token = data
    localStorage.setItem('Token',token)
    
  }


  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans ">
      <form onSubmit={login}>
        <h2>Login</h2>
        <label htmlFor="username">Email</label>
        <input value={email} onChange={(e)=> setEmail(e.target.value)} type="text" placeholder="username" id="username" className="border" />
        <br/>
        <label htmlFor="Password">Password</label>
        <input value={password} onChange={(e)=> setPassword(e.target.value)} type="password" placeholder="Password" id="Password" className="border" /> <br/>
        <span className="text-red">{message}</span> <br/>
        <button type="submit" className="bg-black text-white">Login</button>
      </form>
    </div>
  );
}
