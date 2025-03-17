#!/usr/bin/env bash
#
# Automates the setup of a Django project on Ubuntu:
#   - Updates/installs packages
#   - Creates a virtual environment
#   - Installs Django, Gunicorn, gdown
#   - Creates and configures a new Django project

set -euo pipefail  # Exit on error, undefined variable, or error in a pipeline. 
# The command and options help catch errors early and prevent a script from continuing when something unexpected happens.

########################################
# 1) Update & Install System Packages  #
########################################
echo "==> Updating apt package list and upgrading existing packages..."
sudo apt update -y
sudo apt upgrade -y

echo "==> Installing Python3, pip, venv, and nginx..."
sudo apt install -y python3 python3-pip python3-venv nginx

#############################
# 2) Define Your Variables  #
#############################
# Adjust these variables as needed

# The user who owns the workspace directory
# (Typically your Ubuntu user, e.g., ubuntu for AWS)
USER_NAME="$(ubuntu)"

# Directory to store your Django project and virtual environment
mkdir techProject
cd techProject
DIR_WORKSPACE="/home/${USER_NAME}/techProject"

# Django project name
DJ_PRJ="djangoproject"

# Name of the virtual environment folder
VENV_NAME="env_techProject"

# Superuser credentials (for demonstration only; use stronger creds in production!)
DJANGO_SUPERUSER_USERNAME="admin"
DJANGO_SUPERUSER_EMAIL="admin@example.com"
DJANGO_SUPERUSER_PASSWORD="password123"

echo "==> Configuring environment variables..."
# You can optionally append these to ~/.bashrc so they're available in future shells:
{
  echo ""
  echo "# [Django Setup Script] Environment Variables"
  echo "export DIR_WORKSPACE=\"$DIR_WORKSPACE\""
  echo "export DJ_PRJ=\"$DJ_PRJ\""
  echo "export VENV_NAME=\"$VENV_NAME\""
} >> "${HOME}/.bashrc"

#############################################
# 3) Create Workspace & Python Virtual Env  #
#############################################
echo "==> Creating workspace directory at $DIR_WORKSPACE..."


echo "==> Creating virtual environment ($VENV_NAME)..."
python3 -m venv "$VENV_NAME"

echo "==> Activating virtual environment..."
# Activate in this script. (Note: once this script ends, the venv is deactivated for your shell.)
source "VENV_NAME/bin/activate"

######################################
# 4) Install Django, Gunicorn, gdown #
######################################
echo "==> Upgrading pip and installing Django, Gunicorn, and gdown..."
python -m pip install --upgrade pip
pip install django gunicorn gdown

####################################
# 5) Create & Configure Django App  #
####################################
echo "==> Creating a new Django project: $DJ_PRJ"
# The final "." places the Django project files in the current directory ($DIR_WORKSPACE)
django-admin startproject "$DJ_PRJ" .

echo "==> Applying initial migrations..."
python manage.py migrate

#########################################
# 6) Create Django Superuser (Non-Interactive)
#########################################
echo "==> Creating Django superuser..."
# Export credentials so manage.py can read them
export DJANGO_SUPERUSER_USERNAME DJANGO_SUPERUSER_EMAIL DJANGO_SUPERUSER_PASSWORD
python manage.py createsuperuser --noinput

########################
# 7) Open Port in UFW  #
########################
echo "==> Opening port 8000 in the firewall..."
sudo ufw allow 8000

#####################
# 8) All Done!
#####################
echo ""
echo "==========================================================="
echo " Django project setup is complete!"
echo " Location: $techProject"
echo " Virtual Env: $VENV_NAME"
echo ""
echo " To start using your Django project's virtual environment:"
echo "   cd $techProject"
echo "   source $VENV_NAME/bin/activate"
echo ""
echo " To run the development server (port 8000 by default):"
echo "   python manage.py runserver 0.0.0.0:8000"
echo ""
echo " Remember to reload your shell or run 'source ~/.bashrc'"
echo " if you want the environment variables always available."
echo "==========================================================="
