export interface PaginationIntefaces {
    limit: number,
    offset: number,
    count: number
}


export interface ResponseServer<T> {
    pagination: {
        limit: number
        offset: number
        count: number
    },
    data: T
}
