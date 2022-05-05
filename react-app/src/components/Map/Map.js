import React, { useState, useMemo, useRef } from 'react'

import { GoogleMap, useLoadScript, Marker, MarkerClusterer } from '@react-google-maps/api';
import {
    Combobox,
    ComboboxInput,
    ComboboxPopover,
    ComboboxList,
    ComboboxOption,
    ComboboxOptionText,
} from "@reach/combobox";
import "@reach/combobox/styles.css";
import usePlacesAutocomplete, {
    getGeocode,
    getLatLng
} from 'use-places-autocomplete'

const cityMarkers = [
    {
        city: 'New York',
        lat: 40.776676,
        lng: -73.971321
    },
    {
        city: 'New York',
        lat: 40.816357,
        lng: -73.962898
    },
    {
        city: 'New York',
        lat: 40.650002,
        lng: -73.949997
    },
]

const Maps = ({ apiKey }) => {
    const { isLoaded } = useLoadScript({
        // id: 'google-map-script',
        googleMapsApiKey: apiKey,
        libraries: ['places']
    });

    return (
        <>
            {isLoaded && (
                <Map />
            )}
        </>
    )
}




const containerStyle = {
    width: '400px',
    height: '400px',
}

const Map = () => {
    const [selected, setSelected] = useState(null)
    console.log(selected, 'selected marker')

    const center = useMemo(() => ({
        lat: 38.9072,
        lng: 77.0369,
    }), [])

    return (
        <>
            <div>
                <PlacesAutocomplete setSelected={setSelected} />
            </div>
            <GoogleMap
                mapContainerStyle={containerStyle}
                center={selected ? selected : center}
                zoom={10}
            >
                {selected && (
                    <MarkerClusterer>
                        {(clusterer) =>
                            cityMarkers.map((mark, i) => (
                                <Marker key={i} position={{ lat: mark.lat, lng: mark.lng }} clusterer={clusterer} />
                            ))}
                    </MarkerClusterer>
                )

                }
            </GoogleMap>
        </>
    )
}

const PlacesAutocomplete = ({ setSelected }) => {

    const {
        ready,
        value,
        setValue,
        suggestions: { status, data },
        clearSuggestions
    } = usePlacesAutocomplete()

    const handleSelect = async (address) => {
        setValue(address, false)
        clearSuggestions()

        const results = await getGeocode({ address })
        const { lat, lng } = await getLatLng(results[0])
        setSelected({ lat, lng })
    }

    return (
        <>
            <Combobox onSelect={handleSelect}>
                <ComboboxInput
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    disabled={!ready}
                    placeholder='Search an address'
                />
                <ComboboxPopover>
                    <ComboboxList>
                        {status === 'OK' &&
                            data?.map(({ place_id, description }) => (
                                <ComboboxOption
                                    key={place_id}
                                    value={description}
                                />
                            ))}
                    </ComboboxList>
                </ComboboxPopover>
            </Combobox>
        </>
    )
}

export default React.memo(Maps)
