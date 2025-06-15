import axios from 'axios'
import type {PaginationIntefaces, ResponseServer} from "@/services/Interfaces/BaseIntefaces.ts";
import type {ChannelInterface} from "@/services/Channels/interface.ts";


const channelClient = axios.create({
  baseURL: 'http://127.0.0.1:7980'
})


export async function getChannels(pagination:PaginationIntefaces): Promise<[Error | null, ResponseServer<ChannelInterface[]> ]>{
  try {
      const { data } = await channelClient.get(`/channels/?limit=${pagination.limit}&offset=${pagination.offset}`)
      const response: ResponseServer<ChannelInterface[]> = {
          pagination: {
              limit: data.limit,
              offset: data.offset,
              count: data.count
          },
          data: data.items
      }
      return [null, response as ResponseServer<ChannelInterface[]>]
  }
  catch (error) {
    return [error, null]
  }
}
