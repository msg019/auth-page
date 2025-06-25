import type { RoutesNav, message } from "../interfaces/interfaces"

export const nav:string[]=["Home","Login","Register","Dashboard"]
export const routes: RoutesNav= {
    Home : "/",
    Login: "/login",
    Register: "/register",
    Dashboard: "/dashboard"
}

export const initialMessage:message={
    message:"",
    color: true
}
