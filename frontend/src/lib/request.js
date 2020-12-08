import axios from 'axios'

export const baseURL = 'http://127.0.0.1:5000/'
axios.defaults.withCredentials=true
// create an axios instance
const service = axios.create({
    baseURL: baseURL, // url = base url + request url
    // withCredentials: true, // send cookies when cross-domain requests
    timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
    config => {
        /*
        // do something before request is sent

        if (store.getters.token) {
            // let each request carry token
            // ['X-Token'] is a custom headers key
            // please modify it according to the actual situation
            config.headers['X-Token'] = getToken()
        }
        return config
         */
        console.log("req detected")
        console.log(config)
        return config
    },
    error => {
        // do something with request error
        console.log(error) // for debug
        return Promise.reject(error)
    }
)

// response interceptor
service.interceptors.response.use(
    /**
     * If you want to get http information such as headers or status
     * Please return  response => response
     */

    /**
     * Determine the request status by custom code
     * Here is just an example
     * You can also judge the status by HTTP Status Code
     */
    response => {
        const res = response.data
        // if the custom code is not 20000, it is judged as an error.
        /*
        if (!res.success) {
            //TODO 增加鉴权失败的提示
            throw Error(res.data)
            // console.log('Pro Error')
            // return Promise.reject(new Error(res.data || 'Error'))
        } else {
            return res
        }
         */
        return res
    },
    error => {
        console.log('err' + error) // for debug\
        return Promise.reject(error)
    }
)

export default service
