echo "[*] Sorting out imports"
docker-compose exec api isort src
echo "[*] Formatting code"
docker-compose exec api black src
echo "[*] Checking Flake8"
docker-compose exec api flake8 src
echo "[*] Running test coverage"
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src"
echo "[*] Ops"
sudo chown -R $(whoami) .