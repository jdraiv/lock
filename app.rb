

require 'sinatra'

set :port, '5000'


get '/' do
    'Homepage'
end

get '/room/:name' do |n|
    'Name: %s' % n
end

post '/create_room' do
    'Post'
end