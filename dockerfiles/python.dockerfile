# Use the latest Python image
FROM python:latest

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install -y \
    cron \
    default-mysql-client \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libgtk-3.0 \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install Python packages
RUN pip install discord.py python-dotenv beautifulsoup4 requests mysql-connector-python selenium webdriver-manager openai

# Copy the application files into the container
COPY . .

# Ensure cron logs are available
RUN touch /var/log/cron.log

# Set correct permissions for cron job files
RUN chmod 0644 /etc/cron.d/*

# Start the cron service, apply the cron job, and keep the container running
CMD ["bash", "-c", "chmod 0644 /etc/cron.d/* && crontab /etc/cron.d/bot-cron && cron && tail -f /var/log/cron.log"]
