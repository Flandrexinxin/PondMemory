import request from '@/utils/request'
export function login(email: string, password: string){
  const data = {
    email,
    password
  }
  return request({
    url: 'user/login',
    headers: {
      isToken: false
    },
    method: 'post',
    data: data
  })
}

export function register(userName: string, email: string, password: string, checkCode: string, sessionKey: string){
  const data = {
    userName,
    email,
    password,
    checkCode,
    sessionKey
  }
  return request({
    url: 'user/register',
    headers: {
      isToken: false
    },
    method: 'post',
    data: data
  })
}

export function updatePwd(email: string, password: string, checkCode: string, sessionKey: string){
  const data = {
    email,
    password,
    checkCode,
    sessionKey
  }
  return request({
    url: 'user/updatePwd',
    headers: {
      isToken: false
    },
    method: 'post',
    data: data
  })
}

export function getRegisterSessionKeyCheckCode(userName: string, email: string){
  const data = {
    userName, email,
    "type":"register"
  }
  return request({
    url: 'user/getSessionKeyCheckCode',
    headers: {
      isToken: false
    },
    method: 'post',
    data: data
  })
}

export function getChangePwdSessionKeyCheckCode(email: string){
  const data = {
    email,
    "type":"changePasswd"
  }
  return request({
    url: 'user/getSessionKeyCheckCode',
    headers: {
      isToken: false
    },
    method: 'post',
    data: data
  })
}

export function checkIfEmailIsRegisted(email: string){
  const data = {
    email
  }
  return request({
    url: 'user/register/check',
    headers:{
      isToken: false
    },
    method: 'post',
    data: data
  })
}

export function userProfile(){
  return request({
    url: 'user/profile/get',
    method: 'post'
  })
}

