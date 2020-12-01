mkdir -p ~/.streamlit/

eco "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

