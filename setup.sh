echo "Installing Required Packages..."

pip3 install -U -r ./requirements.txt

echo "Creating environment configuration file"

cp dummy_env.txt .env

echo "Done. Please fill the required fields in .env"

