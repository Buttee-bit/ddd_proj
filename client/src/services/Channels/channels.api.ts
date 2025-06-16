import axios from 'axios'
import type {PaginationIntefaces, ResponseServer} from "@/services/Interfaces/BaseIntefaces.ts";
import type {ChannelInterface} from "@/services/Channels/interface.ts";


const channelClient = axios.create({
    baseURL: 'http://127.0.0.1:7980'
})


export async function getChannels(pagination: PaginationIntefaces): Promise<[Error | null, ResponseServer<ChannelInterface[]>]> {
    try {
        const {data} = await channelClient.get(`/channels/?limit=${pagination.limit}&offset=${pagination.offset}`)
        const response: ResponseServer<ChannelInterface[]> = {
            pagination: {
                limit: data.limit, offset: data.offset, count: data.count
            }, data: data.items
        }
        return [null, response as ResponseServer<ChannelInterface[]>]
    } catch (error) {
        return [error, null]
    }
}

export async function addChannel(url_channel: string) {
    try {
        const {data} = await channelClient.post('/channels/', {'url': url_channel}).da
        const response: ChannelInterface = {
            id_channel:data.id_channel,
            url: data.url,
            oid:data.oid,
            title:data.title,
            subscribers:data.subscribers
        }
        return [null, response]
    } catch (error) {
        return [error, null]
    }
}
