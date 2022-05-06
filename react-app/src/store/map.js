const LOAD_KEY = 'map/load_key'


const loadKey = (key) => {
    return {
        type: LOAD_KEY,
        payload: key
    }
}

export const getKey = () => async (dispatch) => {
    const res = await fetch('/api/map/key', {
        method: 'POST'
    })

    if (res.ok) {

        const data = await res.json()

        dispatch(loadKey(data.googleMapsAPIKey))

    }
}

const initialState = {key: null}

const mapReducer= (state = initialState, action) => {
    switch(action.type){
        case LOAD_KEY:
            return {key: action.payload}
        default:
            return state
    }
}

export default mapReducer;
