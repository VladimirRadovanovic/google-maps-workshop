const LOAD_KEY = 'map/load_key'


const loadKey = (key) => {
    return {
        type: LOAD_KEY,
        key
    }
}

export const getKey = () => async (dispatch) => {
    const res = await fetch('/api/maps/key', {
        method: 'POST'
    })
    const data = await res.json()
    dispatch(loadKey(data.googleMapsAPIKey))
}

const initialState = {key: null}

const mapReducer= (state = initialState, action) => {
    switch(action.type){
        case LOAD_KEY:
            return {key: action.key}
        default:
            return state
    }
}

export default mapReducer;
