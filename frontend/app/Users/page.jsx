'use client'
import Image from "next/image";

export default function Users() {
    
    const GetUsers = async () => {
        const token = localStorage.getItem('Token')
        const response = await fetch('http://127.0.0.1:8000/Users',{
            method:'GET',
            headers:{
                Authorization: `Bearer ${token}`
            }
        })

        const users = await response.json()
        console.log(users)


    }

    return(
        <div>
            <h1>user page</h1>
            <button onClick={GetUsers}>Get users</button>
        </div>
    )
}