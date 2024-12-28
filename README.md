# Docker commands

Build and Publish REST API server

    cd server
    docker build -t quay.io/gaalves/playlists-recommender-server:0.x .
    docker push quay.io/gaalves/playlists-recommender-server:0.x

Build and Publish model

    cd model
    docker build -t quay.io/gaalves/playlists-recommender-model:0.x .
    docker push quay.io/gaalves/playlists-recommender-model:0.x

Run containers

    docker run --name model_container model
    docker run --publish 52023:52023 --name server_container server