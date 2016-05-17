cat <<EOF > secret.yaml
{
    "kind": "Secret",
    "apiVersion": "v1",
    "metadata": {
        "name": "ndslabs-ilb"
    },
    "data": {
        "tls.crt": "$(cat ndslabs.cert | base64)"
        "tls.key": "$(cat ndslabs.key | base64)"
    }
}

EOF
