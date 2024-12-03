from supabase import create_client, Client
from supabase.client import ClientOptions

url = 'https://evewgopleofdphkjwcfs.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV2ZXdnb3BsZW9mZHBoa2p3Y2ZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzMxNzA2MTgsImV4cCI6MjA0ODc0NjYxOH0.2G19pYE4j3fEOZ-SRfQWCkaTl63ORnBIveRGc88vrEU'

supabase: Client = create_client(url, key,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))
